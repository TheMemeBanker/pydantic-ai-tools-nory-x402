# Nory x402 Payment Tools for Pydantic AI

Enable your Pydantic AI agents to make blockchain payments using the x402 HTTP payment protocol.

## Features

- **Multi-chain support**: Solana and 7 EVM chains (Base, Polygon, Arbitrum, Optimism, Avalanche, Sei, IoTeX)
- **Sub-400ms settlement**: Fast payment finality for real-time agent interactions
- **x402 HTTP protocol**: Native support for HTTP 402 Payment Required responses
- **Type-safe**: Full Pydantic validation with TypedDict responses
- **Async-first**: Built with httpx for efficient async operations

## Installation

```bash
pip install pydantic-ai-tools-nory-x402
```

## Quick Start

```python
from pydantic_ai import Agent
from pydantic_ai_tools_nory_x402 import nory_x402_tools

# Create an agent with all payment tools
agent = Agent('openai:gpt-4o', tools=nory_x402_tools())

# Use the agent
result = agent.run_sync("Check if the Nory payment service is healthy")
print(result.data)
```

## Available Tools

### `nory_get_payment_requirements_tool`

Get x402 payment requirements for accessing a paid resource.

```python
from pydantic_ai_tools_nory_x402 import nory_get_payment_requirements_tool

tool = nory_get_payment_requirements_tool()
# Returns: PaymentRequirements with amount, currency, networks, wallet_address
```

### `nory_verify_payment_tool`

Verify a signed payment transaction before settlement.

```python
from pydantic_ai_tools_nory_x402 import nory_verify_payment_tool

tool = nory_verify_payment_tool()
# Returns: VerificationResult with valid, payer, amount
```

### `nory_settle_payment_tool`

Settle a payment on-chain with ~400ms settlement time.

```python
from pydantic_ai_tools_nory_x402 import nory_settle_payment_tool

tool = nory_settle_payment_tool()
# Returns: SettlementResult with success, transaction_id, network
```

### `nory_lookup_transaction_tool`

Look up transaction status.

```python
from pydantic_ai_tools_nory_x402 import nory_lookup_transaction_tool

tool = nory_lookup_transaction_tool()
# Returns: TransactionStatus with status, confirmations, transaction_id
```

### `nory_health_check_tool`

Check Nory service health and see supported networks.

```python
from pydantic_ai_tools_nory_x402 import nory_health_check_tool

tool = nory_health_check_tool()
# Returns: HealthStatus with status, networks
```

### `nory_x402_tools`

Get all tools at once:

```python
from pydantic_ai_tools_nory_x402 import nory_x402_tools

# All tools with optional API key
tools = nory_x402_tools(api_key="your-api-key")
```

## Supported Networks

| Network | Chain Type |
|---------|------------|
| `solana-mainnet` | Solana |
| `solana-devnet` | Solana (testnet) |
| `base-mainnet` | EVM (Base) |
| `polygon-mainnet` | EVM (Polygon) |
| `arbitrum-mainnet` | EVM (Arbitrum) |
| `optimism-mainnet` | EVM (Optimism) |
| `avalanche-mainnet` | EVM (Avalanche) |
| `sei-mainnet` | EVM (Sei) |
| `iotex-mainnet` | EVM (IoTeX) |

## Authentication

For public endpoints, no API key is required. For authenticated endpoints:

```python
tools = nory_x402_tools(api_key="your-api-key")
```

## How It Works

1. Your agent encounters an HTTP 402 Payment Required response
2. Use `nory_get_payment_requirements` to learn how much to pay
3. Sign and encode the payment transaction (client-side)
4. Use `nory_verify_payment` to validate before submission
5. Use `nory_settle_payment` to execute the payment on-chain
6. Access the paid resource with the payment receipt

## Links

- [Nory](https://noryx402.com) - Payment infrastructure for AI agents
- [x402 Protocol](https://www.x402.org/) - HTTP payment protocol specification
- [Pydantic AI](https://ai.pydantic.dev/) - Agent framework for Python

## License

MIT
