load("@rules_python//python:defs.bzl", "py_library", "py_test")

# py_runtime(
#    name = "python3_runtime",
#    files = ["@python_interpreter//:files"],
#    interpreter = "@python_interpreter//:python_bin",
#    python_version = "PY3",
#    visibility = ["//visibility:public"],
# )

# py_runtime_pair(
#    name = "py3_runtime_pair",
#    py2_runtime = None,
#    py3_runtime = ":python3_runtime",
# )

# toolchain(
#    name = "py3_toolchain",
#    toolchain = ":py3_runtime_pair",
#    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
# )

py_test(
    name = "test",
    srcs = ["test.py"],
)

py_library(
    name = "python",
    srcs = [
        "__init__.py",
        "test.py",
    ],
    imports = [".."],
    visibility = ["//:__subpackages__"],
)
