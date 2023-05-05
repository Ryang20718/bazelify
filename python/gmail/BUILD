load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_library(
    name = "gmail",
    srcs = [
        "__init__.py",
        "gmail.py",
    ],
    imports = ["../.."],
    visibility = ["//:__subpackages__"],
)

py_binary(
    name = "gmail_bin",
    srcs = ["__main__.py"],
    imports = ["../.."],
    main = "__main__.py",
    visibility = ["//:__subpackages__"],
)

py_test(
    name = "gmail_test",
    srcs = ["__test__.py"],
    imports = ["../.."],
    main = "__test__.py",
)
