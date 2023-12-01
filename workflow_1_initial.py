from datetime import timedelta

from temporalio import workflow
import asyncio
with workflow.unsafe.imports_passed_through():
    from activities import ssn_trace_activity, SsnTraceInput


@workflow.defn
class BackgroundCheck:
    @workflow.run
    async def run(self, ssn: str) -> str:
        results = await workflow.execute_activity(
            ssn_trace_activity,
            SsnTraceInput(ssn=ssn),
            schedule_to_close_timeout=timedelta(seconds=5),
        )
        await asyncio.sleep(360)
        return results