Build Go Quadrans from Source
=============================

### Most Linux systems and macOS

Go Quadrans is written in [Go][go], so to build from source code you need the most recent version of Go. This guide doesn't cover how to install Go itself, for details read the [Go installation instructions][go-install] and grab any needed bundles from the [Go download page][go-dl].

With Go installed, you can download the project into you `GOPATH` workspace via:

```shell
go get -d github.com/quadrans/go-quadrans
```

You can also install specific versions via:

```shell
go get -d github.com/quadrans/go-quadrans@vXX.XX
```

The above commands do not build any executables. To do that you can either build one specifically:

```shell
go install github.com/quadrans/go-quadrans/cmd/gqdc
```

Or you can build the entire project and install `gqdc` along with all developer tools by running `go install ./...` in the `quadrans/go-quadrans` repository root inside your `GOPATH` workspace.

If you are using macOS and see errors related to macOS header files, install XCode Command Line Tools with `xcode-select --install`, and try again.

If you encounter `go: cannot use path@version syntax in GOPATH mode` or similar errors, enable gomodules using `export GO111MODULE=on`.

### Windows

The Chocolatey package manager provides an easy way to get the required build tools installed. If you don't have chocolatey, [follow the instructions][chocolatey] to install it first.

Then open an Administrator command prompt and install the build tools you need:

```
C:\Windows\system32> choco install git
C:\Windows\system32> choco install golang
C:\Windows\system32> choco install mingw
```

Installing these packages sets up the path environment variables, you need to open a new command prompt to get the new path.

The following steps don't need Administrator privileges. First create and set up a Go workspace directory layout, then clone the source and build it.

```
C:\Users\xxx> mkdir src\github.com\quadrans
C:\Users\xxx> git clone https://github.com/quadrans/go-quadrans src\github.com\quadrans\go-quadrans
C:\Users\xxx> cd src\github.com\quadrans\go-quadrans
C:\Users\xxx\src\github.com\quadrans\go-quadrans> go get -u -v golang.org/x/net/context
C:\Users\xxx\src\github.com\quadrans\go-quadrans> go install -v ./cmd/...
```

### FreeBSD

Clone the repository to a directory of your choosing:

```shell
git clone https://github.com/quadrans/go-quadrans
```

Building `gqdc` requires the Go compiler:

```shell
pkg install go
```

If your golang version is >= 1.5, build the `gqdc` program using the following command:

```shell
cd go-quadrans
make gqdc
```

If your golang version is &lt; 1.5 (quarterly packages, for example), use the following command instead:

```shell
cd go-quadrans
CC=clang make gqdc
```

You can now run `build/bin/gqdc` to start your node.

### Building without a Go workflow

If you do not want to set up Go workspaces on your machine, but only build `gqdc` and forget about the build process, you can clone our repository and use the `make` command, which configures everything for a temporary build and cleans up afterwards. This method of building only works on UNIX-like operating systems, and you still need Go installed.

```shell
git clone https://github.com/quadrans/go-quadrans.git
cd go-quadrans
make gqdc
```

These commands create a `gqdc` executable file in the `go-quadrans/build/bin` folder that you can move wherever you want to run from. The binary is standalone and doesn't require any additional files.

Additionally you can compile all additional tools go-quadrans comes with by running `make all`. 

If you want to cross-compile to another architecture check out the [cross-compilation guide](./cross-compile).

[brew]: https://brew.sh/
[go]: https://golang.org/
[go-dl]: https://golang.org/dl/
[go-install]: https://golang.org/doc/install
[chocolatey]: https://chocolatey.org
[gqdc-releases]: https://github.com/quadrans/go-quadrans/releases
