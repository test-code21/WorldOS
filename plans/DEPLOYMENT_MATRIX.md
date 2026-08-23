# Deployment Matrix

| Capability | Local reference | GCP reference | Must core depend on cloud-specific semantics? |
|---|---|---|---|
| Web/API | container/process | Cloud Run | No |
| Worker/scheduler | container/process | Cloud Run Job/Tasks/Scheduler as appropriate | No |
| PostgreSQL | Docker/local Postgres | Cloud SQL | No |
| Artifact storage | filesystem | Cloud Storage | No |
| Secrets | `.env`/local secret mechanism | Secret Manager | No |
| Logs | stdout/files | Cloud Logging | No |
| Backups | documented DB + artifact procedure | managed DB/storage tooling + documented restore | No |

The GCP path should be excellent, but replacing GCP should not require rewriting domain models.
