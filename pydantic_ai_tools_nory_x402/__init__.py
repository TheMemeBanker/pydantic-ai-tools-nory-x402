"""Nory x402 Payment Tools for Pydantic AI.

This package provides tools for AI agents to make payments using the x402 HTTP protocol.
Supports Solana and 7 EVM chains with sub-400ms settlement.

Example:
    ```python
    from pydantic_ai import Agent
    from pydantic_ai_tools_nory_x402 import nory_x402_tools

    agent = Agent('openai:gpt-4o', tools=nory_x402_tools())
    result = agent.run_sync("Check if the Nory payment service is healthy")
    ```
"""

from pydantic_ai_tools_nory_x402.tools import (
    NoryGetPaymentRequirementsTool,
    NoryHealthCheckTool,
    NoryLookupTransactionTool,
    NorySettlePaymentTool,
    NoryVerifyPaymentTool,
    nory_get_payment_requirements_tool,
    nory_health_check_tool,
    nory_lookup_transaction_tool,
    nory_settle_payment_tool,
    nory_verify_payment_tool,
    nory_x402_tools,
)

__all__ = [
    "NoryGetPaymentRequirementsTool",
    "NoryVerifyPaymentTool",
    "NorySettlePaymentTool",
    "NoryLookupTransactionTool",
    "NoryHealthCheckTool",
    "nory_get_payment_requirements_tool",
    "nory_verify_payment_tool",
    "nory_settle_payment_tool",
    "nory_lookup_transaction_tool",
    "nory_health_check_tool",
    "nory_x402_tools",
]
__version__ = "0.1.0"
