# Hook to build marimo notebooks before Jekyll build
# Place in _plugins/build_marimo_notebooks.rb

Jekyll::Hooks.register :site, :after_init do |site|
  puts "🔧 Building marimo notebooks..."
  
  # Check if marimo is installed
  unless system("which marimo > /dev/null 2>&1") || system("python -m marimo --version > /dev/null 2>&1")
    puts "⚠ Warning: marimo not found. Install with: pip install marimo"
    puts "   Skipping notebook build..."
    next
  end
  
  # Build notebooks
  result = system("python build_notebooks.py 2>&1")
  
  if result && $?.success?
    puts "✓ Marimo notebooks built successfully"
    
    # Verify output exists
    if Dir.exist?("marimo_site") && !Dir.empty?("marimo_site")
      puts "✓ Verified marimo_site directory created"
    else
      puts "⚠ Warning: marimo_site directory not found or empty"
    end
  else
    puts "⚠ Warning: Failed to build marimo notebooks"
    puts "   Site will build without interactive notebooks"
  end
end

Jekyll::Hooks.register :site, :post_write do |site|
  puts "\n📦 Copying marimo notebooks to site..."
  
  # Check if marimo_site exists
  unless Dir.exist?("marimo_site")
    puts "⚠ Skipping: marimo_site directory not found"
    puts "   Run 'python build_notebooks.py' to build notebooks"
    next
  end
  
  # Make script executable
  system("chmod +x copy_notebooks.sh 2>/dev/null")
  
  # Copy notebooks to _site
  result = system("./copy_notebooks.sh 2>&1")
  
  if result && $?.success?
    puts "✓ Notebooks copied to _site"
    
    # Verify critical paths exist
    errors = []
    
    # Check marimo index
    errors << "Missing: _site/marimo.html" unless File.exist?("_site/marimo.html")
    
    # Check for any notebook HTML files
    notebook_count = Dir.glob("_site/**/*.html").select { |f| f.include?("notebooks/") }.length
    if notebook_count == 0
      errors << "No notebook HTML files found in _site"
    else
      puts "✓ Found #{notebook_count} notebook(s)"
    end
    
    if errors.empty?
      puts "✅ All marimo notebooks verified successfully"
    else
      puts "⚠ Verification warnings:"
      errors.each { |err| puts "   - #{err}" }
    end
  else
    puts "⚠ Warning: Failed to copy notebooks"
    puts "   Interactive notebooks may not be accessible"
  end
end
