load("@rules_python//python:defs.bzl", "py_test")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

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

filegroup(
    name = "python_requirements",
    srcs = [
        "requirements.lock",
        "requirements.txt",
    ],
    visibility = ["//visibility:public"],
)

compile_pip_requirements(
    name = "pip_requirements",
    timeout = "moderate",
    extra_args = ["--allow-unsafe"],
    requirements_in = "requirements.txt",
    requirements_txt = "requirements.lock",
    tags = ["manual"],
)
