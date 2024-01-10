FROM golang:1.22-rc-alpine3.18 AS build

WORKDIR /build
COPY hello/go.mod ./hello/
COPY greetings/go.mod ./greetings/
RUN cd hello && go mod download && go mod verify && cd ../greetings && go mod download && go mod verify

WORKDIR /build
COPY hello/hello.go ./hello/
COPY greetings/greeting.go ./greetings/
# Builds the application as a staticly linked one, to allow it to run on alpine
RUN cd hello && GOOS=linux GOARCH=amd64 go build -a -o run .

# Moving the binary to the 'final Image' to make it smaller
FROM alpine:3.19.0

# Create a non-root user
RUN adduser -D -u 1001 appuser

WORKDIR /app
COPY --link --from=build /build/hello/run .

RUN chown appuser:appuser run && chmod +x run

USER 1001

CMD ["/app/run"]