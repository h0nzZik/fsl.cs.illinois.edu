# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "fsl-theme"
  spec.version       = "0.1.0"
  spec.authors       = ["Nishant Rodrigues"]
  spec.email         = ["nishantjr@gmail.com"]

  spec.summary       = "Theme for FSL websites."
  spec.homepage      = "https://fsl.cs.illinois.edu."
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.0"

  spec.add_development_dependency "bundler", "~> 1.16"
  spec.add_development_dependency "rake", "~> 12.0"
end
