---
tags: [chunk, programming-languages, go-cloud]
source: "[[raw-pl-022]]"
---

# chunk-pl-087 Go Cloud Infrastructure Dominance

Go dominates cloud-native infrastructure. The reasons align with Go's design:

**Key projects in Go:**
- **Docker:** Container runtime
- **Kubernetes:** Container orchestration
- **Terraform:** Infrastructure as code
- **etcd:** Distributed key-value store
- **Prometheus:** Monitoring and alerting
- **Grafana:** Observability dashboards
- **CockroachDB:** Distributed SQL database
- **Hugo:** Static site generator
- **Caddy:** Web server with automatic HTTPS

**Why Go wins here:**
1. Static binaries — deploy by copying a file
2. Fast compilation — rapid CI/CD cycles
3. Goroutines — handle thousands of concurrent connections
4. Standard library — net/http, encoding/json, crypto built in
5. Cross-compilation — build for any OS/arch from any OS/arch
6. Readability — large rotating teams (cloud companies) can onboard quickly

**The deployment story:** GOOS=linux GOARCH=amd64 go build produces a Linux binary from any machine. Copy to server. Done. No runtime, no dependencies, no Docker needed (though Go is what Docker is written in).
