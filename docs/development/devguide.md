Developer Guide
=============================

**NOTE: These instructions are for people who want to contribute Go source code changes. If you just want to run a Quadrans Node, use the regular [Installation Instructions](../nodes/index).**

This document is the entry point for developers of the Go implementation of Quadrans.

Developers here refer to the hands-on: who are interested in build, develop, debug, submit a bug report or pull request or contribute code to go-quadrans.

## Contributing

Thank you for considering to help out with the source code! We welcome contributions from anyone on the internet, and are grateful for even the smallest of fixes!

GitHub is used to track issues and contribute code, suggestions, feature requests or documentation.

If you'd like to contribute to go-quadrans, please fork, fix, commit and send a pull request (PR) for the maintainers to review and merge into the main code base. If you wish to submit more complex changes though, please check up with the core devs in the [Quadrans Discord Server](https://discord.gg/2bMpuU9Z) to ensure those changes are in line with the general philosophy of the project and/or get some early feedback. 

This can reduce your effort as well as speeding up our review and merge procedures.

PRs need to be based on and opened against the `main` branch (unless by explicit agreement, you contribute to a complex feature branch).

We encourage a PR early approach, meaning you create the PR the earliest even without the fix/feature. This will let core devs and other volunteers know you picked up an issue.

These early PRs should indicate 'in progress' status.

## Building and Testing

We assume that you have Go installed. Please use Go version 1.13 or later. We use the gc toolchain for development, which you can get from the [Go downloads page](https://golang.org/doc/install).

go-quadrans is a Go module, and uses the [Go modules system](https://github.com/golang/go/wiki/Modules) to manage dependencies. Using `GOPATH` is not required to build go-quadrans.

### Building Executables

Switch to the go-quadrans repository root directory.

You can build all code using the go tool, placing the resulting binary in `$GOPATH/bin`.

```text
go install -v ./...
```

go-quadrans exectuables can be built individually. To build just gqdc, use:

```text
go install -v ./cmd/gqdc
```

If you want to compile gqdc for an architecture that differs from your host, please consult our [cross compilation guide](../nodes/build/cross-compile).

### Testing

Testing a package:

```
go test -v ./qdc
```

Running an individual test:

```
go test -v ./qdc -run TestMethod
```

**Note**: here all tests with prefix _TestMethod_ will be run, so if you got TestMethod, TestMethod1, then both tests will run.

Running benchmarks, eg.:

```
go test -v -bench . -run BenchmarkJoin
```

For more information, see the [go test flags](https://golang.org/cmd/go/#hdr-Testing_flags) documentation.

### Getting Stack Traces

If `gqdc` is started with the `--pprof` option, a debugging HTTP server is made available on port 6060. You can bring up <http://localhost:6060/debug/pprof> to see the heap, running routines etc. By clicking "full goroutine stack dump" you can generate a trace that is useful for debugging.

Note that if you run multiple instances of `gqdc`, this port will only work for the first instance that was launched. If you want to generate stacktraces for these other instances, you need to start them up choosing an alternative pprof port. Make sure you are redirecting stderr to a logfile.

```
gqdc -port=30300 -verbosity 5 --pprof --pprof.port 6060 2>> /tmp/00.glog
gqdc -port=30301 -verbosity 5 --pprof --pprof.port 6061 2>> /tmp/01.glog
gqdc -port=30302 -verbosity 5 --pprof --pprof.port 6062 2>> /tmp/02.glog
```

Alternatively if you want to kill the clients (in case they hang or stalled syncing, etc) and have the stacktrace too, you can use the `-QUIT` signal with `kill`:

```
killall -QUIT gqdc
```

This will dump stack traces for each instance to their respective log file.
