# Hook to build marimo notebooks before Jekyll build
# Place in _plugins/build_marimo_notebooks.rb

def should_rebuild_notebooks?
  # Skip rebuild in CI if marimo_site already exists (built in previous step)
  if ENV['CI'] && Dir.exist?("marimo_site") && !Dir.glob("marimo_site/**/*.html").empty?
    return false
  end
  
  # Check if source notebooks are newer than built HTML files
  source_notebooks = Dir.glob("notebooks/**/*.py") + Dir.glob("projects/**/notebooks/**/*.py")
  return true if source_notebooks.empty? # No notebooks found, skip rebuild
  
  return true unless Dir.exist?("marimo_site") # marimo_site doesn't exist, need to build
  
  built_html = Dir.glob("marimo_site/**/*.html")
  return true if built_html.empty? # No built HTML, need to build
  
  # Compare modification times
  newest_source = source_notebooks.map { |f| File.mtime(f) }.max
  oldest_built = built_html.map { |f| File.mtime(f) }.min
  
  newest_source > oldest_built
end

Jekyll::Hooks.register :site, :after_init do |site|
  # Check if marimo is installed
  unless system("which marimo > /dev/null 2>&1") || system("python -m marimo --version > /dev/null 2>&1")
    puts "⚠ Warning: marimo not found. Install with: pip install marimo"
    puts "   Skipping notebook build..."
    next
  end
  
  # Check if rebuild is needed
  if should_rebuild_notebooks?
    puts "🔧 Building marimo notebooks..."
    
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
  else
    puts "ℹ Marimo notebooks are up to date, skipping rebuild"
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
