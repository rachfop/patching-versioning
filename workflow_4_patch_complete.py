from datetime import timedelta

from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import ssn_trace_activity, federal_background_check_activity, SsnTraceInput


@workflow.defn
class BackgroundCheck:
    @workflow.run
    async def run(self) -> None:
        # Updated logic, post-patch deprecation
        results = await workflow.execute_activity(
            ssn_trace_activity,
            SsnTraceInput(ssn=ssn),
            schedule_to_close_timeout=timedelta(seconds=5),
        )
        if results == "pass":
            return await workflow.execute_activity(
                federal_background_check_activity,
                SsnTraceInput(ssn=ssn),
                schedule_to_close_timeout=timedelta(seconds=5),
            )
        else:
            return results
