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

BAZEL_ZIG_CC_VERSION = "v1.0.1"

http_archive(
    name = "bazel-zig-cc",
    sha256 = "e9f82bfb74b3df5ca0e67f4d4989e7f1f7ce3386c295fd7fda881ab91f83e509",
    strip_prefix = "bazel-zig-cc-{}".format(BAZEL_ZIG_CC_VERSION),
    urls = [
        "https://mirror.bazel.build/github.com/uber/bazel-zig-cc/releases/download/{0}/{0}.tar.gz".format(BAZEL_ZIG_CC_VERSION),
        "https://github.com/uber/bazel-zig-cc/releases/download/{0}/{0}.tar.gz".format(BAZEL_ZIG_CC_VERSION),
    ],
)

load("@bazel-zig-cc//toolchain:defs.bzl", zig_toolchains = "toolchains")

zig_toolchains()

register_toolchains(
    "@zig_sdk//toolchain:linux_amd64_gnu.2.19",
    "@zig_sdk//toolchain:linux_arm64_gnu.2.28",
    "@zig_sdk//toolchain:darwin_amd64",
    "@zig_sdk//toolchain:darwin_arm64",
    "@zig_sdk//toolchain:windows_amd64",
    "@zig_sdk//toolchain:windows_arm64",
)

## PYTHON
http_archive(
    name = "rules_python",
    sha256 = "94750828b18044533e98a129003b6a68001204038dc4749f40b195b24c38f49f",
    strip_prefix = "rules_python-0.21.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_10",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.10",
)

load("@python3_10//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip",
    python_interpreter_target = interpreter,
    requirements_lock = "//python:requirements.lock",
)

load("@pip//:requirements.bzl", "install_deps")

# Initialize repositories for all packages in requirements_lock.txt.
install_deps()
# # GOLANG
# http_archive(
#     name = "io_bazel_rules_go",
#     sha256 = "6b65cb7917b4d1709f9410ffe00ecf3e160edf674b78c54a894471320862184f",
#     urls = [
#         "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
#         "https://github.com/bazelbuild/rules_go/releases/download/v0.39.0/rules_go-v0.39.0.zip",
#     ],
# )

# http_archive(
#     name = "bazel_gazelle",
#     sha256 = "ecba0f04f96b4960a5b250c8e8eeec42281035970aa8852dda73098274d14a1d",
#     urls = [
#         "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.29.0/bazel-gazelle-v0.29.0.tar.gz",
#         "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.29.0/bazel-gazelle-v0.29.0.tar.gz",
#     ],

# )
# load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
# load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies", "go_repository")

# ############################################################
# # Define your own dependencies here using go_repository.
# # Else, dependencies declared by rules_go/gazelle will be used.
# # The first declaration of an external repository "wins".
# ############################################################

# go_rules_dependencies()

# go_register_toolchains(version = "1.19.5")

# gazelle_dependencies()

# load("@bazel_gazelle//:def.bzl", "gazelle")

# # gazelle:prefix github.com/example/project
# gazelle(name = "gazelle")
