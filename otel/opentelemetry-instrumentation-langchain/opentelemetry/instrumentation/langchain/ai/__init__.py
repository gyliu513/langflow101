from enum import Enum


class SpanAttributes:
    # LLM
    LLM_VENDOR = "llm.vendor"
    LLM_REQUEST_TYPE = "llm.request.type"
    LLM_REQUEST_MODEL = "llm.request.model"
    LLM_RESPONSE_MODEL = "llm.response.model"
    LLM_REQUEST_MAX_TOKENS = "llm.request.max_tokens"
    LLM_USAGE_TOTAL_TOKENS = "llm.usage.total_tokens"
    LLM_USAGE_COMPLETION_TOKENS = "llm.usage.completion_tokens"
    LLM_USAGE_PROMPT_TOKENS = "llm.usage.prompt_tokens"
    LLM_TEMPERATURE = "llm.temperature"
    LLM_TOP_P = "llm.top_p"
    LLM_TOP_K = "llm.top_k"
    LLM_FREQUENCY_PENALTY = "llm.frequency_penalty"
    LLM_PRESENCE_PENALTY = "llm.presence_penalty"
    LLM_PROMPTS = "llm.prompts"
    LLM_COMPLETIONS = "llm.completions"
    LLM_CHAT_STOP_SEQUENCES = "llm.chat.stop_sequences"

    # Watson LLM
    LLM_WATSON_MAX_NEW_TOKENS = "llm.watson.max_new_tokens"
    LLM_WATSON_MIN_NEW_TOKENS = "llm.watson.min_new_tokens"
    LLM_WATSON_DECODING_METHOD = "llm.watson.decoding_method"
    LLM_WATSON_PROJECT_ID = "llm.watson.project_id"
    LLM_WATSON_RANDOM_SEED = "llm.watson.random_seed"
    LLM_WATSON_REPETITION_PENALTY = "llm.watson.repetition_penalty"
    LLM_WATSON_TIME_LIMIT = "llm.watson.time_limit"
    LLM_WATSON_TRUNCATE_INPUT_TOKENS = "llm.watson.truncate_input_tokens"
    LLM_WATSON_LENGTH_PENALTY = "llm.watson.length_penalty"
    LLM_WATSON_RETURN_OPTIONS = "llm.watson.return_options"
    
    # Vector DB
    VECTOR_DB_VENDOR = "vector_db.vendor"
    VECTOR_DB_QUERY_TOP_K = "vector_db.query.top_k"

    # LLM Workflows
    TRACELOOP_SPAN_KIND = "traceloop.span.kind"
    TRACELOOP_WORKFLOW_NAME = "traceloop.workflow.name"
    TRACELOOP_ENTITY_NAME = "traceloop.entity.name"
    TRACELOOP_ASSOCIATION_PROPERTIES = "traceloop.association.properties"

    # Deprecated
    TRACELOOP_CORRELATION_ID = "traceloop.correlation.id"


class LLMRequestTypeValues(Enum):
    COMPLETION = "completion"
    CHAT = "chat"
    RERANK = "rerank"
    UNKNOWN = "unknown"


class TraceloopSpanKindValues(Enum):
    WORKFLOW = "workflow"
    TASK = "task"
    AGENT = "agent"
    TOOL = "tool"
    UNKNOWN = "unknown"
