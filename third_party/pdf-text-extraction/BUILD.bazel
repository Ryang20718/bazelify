load("@rules_foreign_cc//foreign_cc:defs.bzl", "cmake")

filegroup(
    name = "all_srcs",
    srcs = glob(
        ["**"],
        exclude = [
            "**/.gitignore",
            ".trunk/.gitignore",
            "pdfhummus-populate/**/.gitignore",
            "pdfhummus-populate/.gitignore",
        ],
    ),
    visibility = ["//visibility:public"],
)

cmake(
    name = "pdf-text-extraction",
    build_args = [
        "--build",
        "build",
        "--config",
        "release",
    ],
    cache_entries = {
        "CMAKE_C_FLAGS": "-fPIC",
    },
    lib_source = ":all_srcs",
    out_include_dir = "include",
    visibility = ["//visibility:public"],
)
