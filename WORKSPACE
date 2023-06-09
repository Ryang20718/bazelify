load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "b8a1527901774180afc798aeb28c4634bdccf19c4d98e7bdd1ce79d1fe9aaad7",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.1/bazel-skylib-1.4.1.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.1/bazel-skylib-1.4.1.tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()

# BAZEL_ZIG_CC_VERSION = "v1.0.1"

# http_archive(
#     name = "bazel-zig-cc",
#     sha256 = "e9f82bfb74b3df5ca0e67f4d4989e7f1f7ce3386c295fd7fda881ab91f83e509",
#     strip_prefix = "bazel-zig-cc-{}".format(BAZEL_ZIG_CC_VERSION),
#     urls = [
#         "https://mirror.bazel.build/github.com/uber/bazel-zig-cc/releases/download/{0}/{0}.tar.gz".format(BAZEL_ZIG_CC_VERSION),
#         "https://github.com/uber/bazel-zig-cc/releases/download/{0}/{0}.tar.gz".format(BAZEL_ZIG_CC_VERSION),
#     ],
# )

# load("@bazel-zig-cc//toolchain:defs.bzl", zig_toolchains = "toolchains")

# zig_toolchains()

# register_toolchains(
#     "@zig_sdk//toolchain:linux_amd64_gnu.2.19",
#     "@zig_sdk//toolchain:linux_arm64_gnu.2.28",
#     "@zig_sdk//toolchain:darwin_amd64",
#     "@zig_sdk//toolchain:darwin_arm64",
#     "@zig_sdk//toolchain:windows_amd64",
#     "@zig_sdk//toolchain:windows_arm64",
# )

# GCC
http_archive(
    name = "aspect_gcc_toolchain",
    sha256 = "3341394b1376fb96a87ac3ca01c582f7f18e7dc5e16e8cf40880a31dd7ac0e1e",
    strip_prefix = "gcc-toolchain-0.4.2",
    url = "https://github.com/aspect-build/gcc-toolchain/archive/refs/tags/0.4.2.tar.gz",
)

load("@aspect_gcc_toolchain//toolchain:defs.bzl", "ARCHS", "gcc_register_toolchain")

gcc_register_toolchain(
    name = "gcc_toolchain_aarch64",
    gcc_version = "10.3.0",
    sysroot_variant = "aarch64",
    target_arch = ARCHS.aarch64,
)

### GOLANG ###
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "6b65cb7917b4d1709f9410ffe00ecf3e160edf674b78c54a894471320862184f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
    ],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "ecba0f04f96b4960a5b250c8e8eeec42281035970aa8852dda73098274d14a1d",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.29.0/bazel-gazelle-v0.29.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.29.0/bazel-gazelle-v0.29.0.tar.gz",
    ],
)

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")
load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.19.5")

gazelle_dependencies()

## PYTHON
http_archive(
    name = "rules_python",
    sha256 = "94750828b18044533e98a129003b6a68001204038dc4749f40b195b24c38f49f",
    strip_prefix = "rules_python-0.21.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
)

http_archive(
    name = "rules_python_gazelle_plugin",
    sha256 = "94750828b18044533e98a129003b6a68001204038dc4749f40b195b24c38f49f",
    strip_prefix = "rules_python-0.21.0/gazelle",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
)

# Next we load the toolchain from rules_python.
load("@rules_python//python:repositories.bzl", "python_register_toolchains")

# We now register a hermetic Python interpreter rather than relying on a system-installed interpreter.
# This toolchain will allow bazel to download a specific python version, and use that version
# for compilation.
python_register_toolchains(
    name = "python310",
    python_version = "3.10",
)

# Load the interpreter and pip_parse rules.
load("@python310//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

# This macro wraps the `pip_repository` rule that invokes `pip`, with `incremental` set.
# Accepts a locked/compiled requirements file and installs the dependencies listed within.
# Those dependencies become available in a generated `requirements.bzl` file.
# You can instead check this `requirements.bzl` file into your repo.
pip_parse(
    name = "pip",
    # Generate user friendly alias labels for each dependency that we have.
    incompatible_generate_aliases = True,
    python_interpreter_target = interpreter,
    # Set the location of the lock file.
    requirements_lock = "//:requirements.lock",
)

# Load the install_deps macro.
load("@pip//:requirements.bzl", "install_deps")

# Initialize repositories for all packages in requirements_lock.txt.
install_deps()

# The rules_python gazelle extension has some third-party go dependencies
# which we need to fetch in order to compile it.
load("@rules_python_gazelle_plugin//:deps.bzl", _py_gazelle_deps = "gazelle_deps")

# See: https://github.com/bazelbuild/rules_python/blob/main/gazelle/README.md
# This rule loads and compiles various go dependencies that running gazelle
# for python requirements.
_py_gazelle_deps()

## CMAKE Tools

http_archive(
    name = "rules_foreign_cc",
    sha256 = "2a4d07cd64b0719b39a7c12218a3e507672b82a97b98c6a89d38565894cf7c51",
    strip_prefix = "rules_foreign_cc-0.9.0",
    url = "https://github.com/bazelbuild/rules_foreign_cc/archive/refs/tags/0.9.0.tar.gz",
)

load("@rules_foreign_cc//foreign_cc:repositories.bzl", "rules_foreign_cc_dependencies")

# This sets up some common toolchains for building targets. For more details, please see
# https://bazelbuild.github.io/rules_foreign_cc/0.9.0/flatten.html#rules_foreign_cc_dependencies
rules_foreign_cc_dependencies()

http_archive(
    name = "pdf-text-extraction",
    build_file = "//third_party/pdf-text-extraction:BUILD",
    sha256 = "bd66935a261e96e70893da700355b56adbc5a02a860cbdc2d9bfbb6801cc91cd",
    strip_prefix = "pdf-text-extraction-1.1",
    url = "https://github.com/galkahana/pdf-text-extraction/archive/refs/tags/v1.1.tar.gz",
)

http_archive(
    name = "rules_rust",
    sha256 = "50272c39f20a3a3507cb56dcb5c3b348bda697a7d868708449e2fa6fb893444c",
    urls = [
        "https://github.com/bazelbuild/rules_rust/releases/download/0.22.0/rules_rust-v0.22.0.tar.gz",
    ],
)

load("@rules_rust//rust:repositories.bzl", "rules_rust_dependencies", "rust_analyzer_toolchain_repository", "rust_register_toolchains")

RUST_VERSION = "1.68.0"

# Adds the necessary dependencies for the Rust rules.
rules_rust_dependencies()

# Registers Rust toolchains with the given versions and editions.
rust_register_toolchains(
    # Specifies the Rust edition to use for the registered toolchains.
    edition = "2021",
    versions = [RUST_VERSION],
)

load("@rules_rust//tools/rust_analyzer:deps.bzl", "rust_analyzer_dependencies")

rust_analyzer_dependencies()

register_toolchains(rust_analyzer_toolchain_repository(
    name = "rust_analyzer_toolchain",
    # This should match the currently registered toolchain.
    version = "1.68.0",
))

# Raze

load("//cargo:crates.bzl", "raze_fetch_remote_crates")

raze_fetch_remote_crates()
