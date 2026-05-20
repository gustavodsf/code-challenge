// app.js — single file, ready for HackerRank
const express = require("express");

//
// === rateLimiterOptions ===
//
const rateLimiterOptions = {
  maxRequests: 5,
  timeWindow: 1000, // 1 second
};

//
// === RateLimiterMiddleware ===
//
class RateLimiterMiddleware {
  constructor(options) {
    this.maxRequests = options.maxRequests;
    this.timeWindow = options.timeWindow;
    this.clients = new Map();
  }

  middleware() {
    return (req, res, next) => {
      const ip =
        req.ip ||
        req.connection?.remoteAddress ||
        req.socket?.remoteAddress ||
        "unknown";

      const now = Date.now();
      let record = this.clients.get(ip);

      if (!record) {
        record = { count: 0, first: now };
      }

      const elapsed = now - record.first;

      if (elapsed >= this.timeWindow) {
        record.count = 0;
        record.first = now;
      }

      record.count += 1;
      this.clients.set(ip, record);

      const remaining = Math.max(this.maxRequests - record.count, 0);
      const reset = record.first + this.timeWindow;

      // Required headers
      res.setHeader("X-RateLimit-Limit", this.maxRequests);
      res.setHeader("X-RateLimit-Remaining", remaining);
      res.setHeader("X-RateLimit-Reset", reset);

      // allow maxRequests, block when exceeded
      if (record.count > this.maxRequests) {
        res.setHeader("X-RateLimit-Remaining", 0);
        return res
          .status(429)
          .json({ message: "You have exceeded the rate limit. Please try again later." });
      }

      next();
    };
  }

  reset() {
    this.clients.clear();
  }
}

//
// === Express Application ===
//
const app = express();
app.set("trust proxy", true);

// ✅ use middleware correctly
const rateLimiter = new RateLimiterMiddleware(rateLimiterOptions);
app.use(rateLimiter.middleware()); // <‑‑ must call .middleware()

// Base routes
app.get("/", (req, res) => {
  res.send("<p>Welcome to the rate-limited API!</p>");
});

app.get("/api", (req, res) => {
  res.json({ message: "Welcome to the rate-limited API!" });
});

// Export for tests
module.exports = app;

// If run directly, start server
if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
}

// Also export these because the test harness expects them
module.exports.rateLimiterOptions = rateLimiterOptions;
module.exports.RateLimiterMiddleware = RateLimiterMiddleware;