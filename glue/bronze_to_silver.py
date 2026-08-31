import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "SOURCE_PATH",
        "SILVER_BASE_PATH",
        "REJECT_BASE_PATH",
        "TARGET_YEAR",
        "TARGET_MONTH",
        "TARGET_DAY",
        "TARGET_HOUR",
        "OUTPUT_PARTITIONS",
    ],
)

print(f"Starting Bronze to Silver ETL Job: {args['JOB_NAME']}")
print(f"Target date/hour: {args['TARGET_YEAR']}-{args['TARGET_MONTH']}-{args['TARGET_DAY']} {args['TARGET_HOUR']}:00")
