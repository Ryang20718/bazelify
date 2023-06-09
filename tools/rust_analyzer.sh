#!/bin/bash

tools/bazel run "@rules_rust//tools/rust_analyzer:gen_rust_project"

# restart rust-analyzer if running
killall rust-analyzer || true