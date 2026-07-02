---
tags: [stock-trading, moc]
up: "[[Welcome]]"
confidence: verified
freshness: current-sensitive
last-verified: 2026-07-02
tier-coverage: [core, practice]
---
# Stock Trading

> A ground-up stock-market learning wiki: ownership, market mechanics, account rules, company analysis, risk control, and paper-trading practice before live capital.

> Education only. These notes are not financial advice, trade recommendations, tax advice, or legal advice. Before any real transaction, refresh the current rules from the linked SEC/Investor.gov, FINRA, broker, and tax sources.

## Start Here

- [[Stock Trading - Learning Path]] - progressive route from vocabulary to paper-trading discipline
- [[Stock Trading Book Reading Spine]] - book-style route through the topic
- [[Stock Trading Study Index]] - drills, recall prompts, and first practice loop
- [[Stock Trading/Sources/Sources Index|Sources Index]] - official source layer for this domain

## Domain Hubs

### Foundations

- [[Stocks and Ownership]] - what a share represents, why stocks can return money, and what public-company reporting makes visible
- [[Returns Risk and Time Horizon]] - why time horizon, volatility, diversification, and capital-at-risk must come before strategy

### Market Mechanics

- [[How Stock Markets Work]] - brokers, quotes, bid/ask spreads, liquidity, and market-wide safeguards
- [[Order Types and Execution]] - market, limit, stop, and stop-limit orders as execution tools rather than prediction tools
- [[Accounts Settlement and Margin]] - cash accounts, margin accounts, T+1 settlement, intraday margin, and short-sale constraints

### Analysis

- [[Reading Company Filings and Fundamentals]] - 10-K, 10-Q, EDGAR, business model, risk factors, financial statements, and valuation ratios
- [[Company Filing Worksheet]] - turn one filing into a bounded thesis before a chart read or paper trade
- [[Price Action Momentum and Volatility]] - chart vocabulary, momentum, beta, volatility, and why price action is a risk surface

### Strategies

- [[Quantitative Trading]] - model-driven research, backtesting boundaries, model risk, and research journaling
- [[Algorithmic Trading]] - automation, order-generation controls, kill switches, and paper-only simulation boundaries
- [[Backtesting and Simulation]] - historical replay, simulation ladder, cost assumptions, and rejection rules
- [[Market Data and Data Quality]] - dataset cards, timestamps, point-in-time safety, and missing-data rules
- [[Broker APIs and Automation Controls]] - paper-only API boundaries, credential safety, limits, logs, and kill switches

### Risk Process

- [[Position Sizing and Trade Journaling]] - convert a thesis into a bounded experiment with entry, invalidation, size, exit, and review
- [[Paper Trading Lab]] - ten-trade paper batch for testing decision quality without live capital

## Operating Rules

1. Learn the market object before learning the button: stock, broker, order, settlement, account type, and risk.
2. Treat every trade as a hypothesis with a known maximum planned loss before entry.
3. Do not use margin, short selling, or options in the first pass.
4. Use [[Paper Trading Lab|paper trading]] and historical examples until the journal can show repeatable decision quality.
5. Refresh current rules before applying anything involving settlement, margin, day trading, or taxes.
6. Treat [[Quantitative Trading|quantitative]] and [[Algorithmic Trading|algorithmic]] strategies as advanced research artifacts until manual risk, order, and journal discipline are stable.

## Current-Rules Watchlist

These topics are current-sensitive and must be rechecked before use:

- U.S. settlement cycle: the standard cycle for covered securities moved to T+1 for applicable transactions on or after May 28, 2024.
- Intraday margin: FINRA published new risk-based intraday margin guidance in 2026, replacing the older pattern-day-trader framing in key investor education material.
- Broker-specific margin, order-routing, short-locate, cash-sweep, and fee rules.
- Algorithmic trading, market access, automated order controls, and broker API behavior.
- Tax treatment of short-term gains, wash sales, dividends, and account type.

## References

- [[Stock Trading/Sources/Sources Index|Sources Index]]
- [[Stock Trading Book Reading Spine]]
- [[Paper Trading Lab]]
- [[Quantitative Trading]]
- [[Algorithmic Trading]]
- [[Backtesting and Simulation]]
- [[Market Data and Data Quality]]
- [[Broker APIs and Automation Controls]]
- [Investor.gov - Introduction to Investing](https://www.investor.gov/introduction-investing)
- [Investor.gov - Stocks](https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks)
- [Investor.gov - New T+1 Settlement Cycle](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin)
- [FINRA - Frequent Intraday Trading](https://www.finra.org/investors/insights/frequent-intraday-trading)
- [FINRA - Understanding the New Intraday Margin Requirements](https://www.finra.org/investors/insights/intraday-margin-requirements)
