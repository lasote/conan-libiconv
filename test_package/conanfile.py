from conans.model.conan_file import ConanFile
from conans import CMake
import os


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "libiconv/1.14@lasote/stable"

    def build(self):
        cmake = CMake(self.settings)
        # Current dir is "test_package/build/{build_id}" and CMakeLists.txt is in "test_package"
        cmake.configure(self, source_dir="../../", build_dir="./")
        cmake.build(self)

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib", dst="bin", src="lib")
        
    def test(self):
        self.run(".%sbin%sexample --help" % (os.sep, os.sep))
