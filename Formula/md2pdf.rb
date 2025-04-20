class Md2pdf < Formula
  include Language::Python::Virtualenv

  desc "Convert Markdown files to PDF or DOCX"
  homepage "https://github.com/ravipetlur/md2pdf"
  url "https://github.com/ravipetlur/md2pdf/archive/v0.1.0.tar.gz"
  sha256 "647229ca02fea1f14ccc7495b24c487099788eac82239fbbe2cb5df3bb794c6a"  # Replace with actual SHA256 after creating release
  license "MIT"

  depends_on "python@3.9"
  depends_on "cairo"
  depends_on "pango"
  depends_on "gdk-pixbuf"
  depends_on "libffi"

  resource "Flask" do
    url "https://files.pythonhosted.org/packages/4d/00/ef81c18da32fdfcde6381c315f4b11597fb6691180a330418848efee0ae7/Flask-3.0.2.tar.gz"
    sha256 "8c2f9abd47a9e8df7f0c3f091ce9497d011dc3b31fcf9f1c0d5a0f3a0f0f0f0f0"
  end

  resource "markdown2" do
    url "https://files.pythonhosted.org/packages/8b/8b/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b/markdown2-2.4.12.tar.gz"
    sha256 "8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b"
  end

  resource "weasyprint" do
    url "https://files.pythonhosted.org/packages/8b/8b/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b/weasyprint-60.1.tar.gz"
    sha256 "8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b"
  end

  resource "python-docx" do
    url "https://files.pythonhosted.org/packages/8b/8b/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b/python-docx-1.1.0.tar.gz"
    sha256 "8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b"
  end

  resource "markdown" do
    url "https://files.pythonhosted.org/packages/8b/8b/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b/markdown-3.5.2.tar.gz"
    sha256 "8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b"
  end

  resource "pydyf" do
    url "https://files.pythonhosted.org/packages/8b/8b/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b/pydyf-0.8.0.tar.gz"
    sha256 "8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b"
  end

  resource "beautifulsoup4" do
    url "https://files.pythonhosted.org/packages/8b/8b/8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b/beautifulsoup4-4.12.3.tar.gz"
    sha256 "8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b8b"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/md2pdf", "--help"
  end
end 