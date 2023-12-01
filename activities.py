from temporalio import activity
from dataclasses import dataclass

@dataclass
class SsnTraceInput:
    ssn: str

@activity.defn
async def ssn_trace_activity(input_data: SsnTraceInput) -> str:
    return "pass"

@activity.defn
async def federal_background_check_activity(input_data: SsnTraceInput) -> str:
    return "pass"
