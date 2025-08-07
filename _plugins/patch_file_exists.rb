# ensure File.exists? still works under Ruby 3.x
class File
  class << self
    alias exists? exist? unless method_defined?(:exists?)
  end
end

