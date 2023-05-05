load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "claude",
    srcs = [
        "__init__.py",
        "claude.py",
    ],
    imports = ["../.."],
    visibility = ["//:__subpackages__"],
    deps = [
        "@pip//anthropic",
        "@pip//requests",
    ],
)

py_binary(
    name = "claude_bin",
    srcs = ["__main__.py"],
    imports = ["../.."],
    main = "__main__.py",
    visibility = ["//:__subpackages__"],
)

py_test(
    name = "claude_test",
    srcs = ["__test__.py"],
    imports = ["../.."],
    main = "__test__.py",
)
