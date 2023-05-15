load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "document_processing",
    srcs = ["document_processing.py"],
    imports = ["../.."],
    visibility = ["//:__subpackages__"],
    deps = [
        "@pip//pdf2image",
        "@pip//pillow",
        "@pip//pytesseract",
        "@pip//torch",
        "@pip//transformers",
    ],
)
