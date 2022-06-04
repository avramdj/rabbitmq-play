FROM golang:1.18.2-alpine3.15 AS build

WORKDIR /app
COPY . .
RUN go build -o run

FROM alpine:3.15 as runtime

WORKDIR /app
COPY --from=build /app/run .

CMD ["./run"]
