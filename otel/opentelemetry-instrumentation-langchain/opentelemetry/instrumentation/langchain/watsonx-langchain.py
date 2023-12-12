"""Langchain BaseHandler instrumentation"""
import logging
from typing import Collection

from opentelemetry.trace import get_tracer
from opentelemetry.instrumentation.langchain.version import __version__
from opentelemetry.semconv.ai import TraceloopSpanKindValues
from otel_lib.instrumentor import LangChainHandlerInstrumentor


logger = logging.getLogger(__name__)

_instruments = ("langchain >= 0.0.200",)


from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

os.environ['OTEL_EXPORTER_OTLP_INSECURE'] = 'True'

import sys

from opentelemetry import trace
# from opentelemetry.instrumentation.wsgi import collect_request_attributes
from opentelemetry.propagate import extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import (
    SpanKind,
    get_tracer_provider,
    set_tracer_provider,
)

tracer_provider = TracerProvider(
    resource=Resource.create({'service.name': os.environ["SVC_NAME"]}),
)

# Create an OTLP Span Exporter
otlp_exporter = OTLPSpanExporter(
    endpoint=os.environ["OTLP_EXPORTER"]+":4317",  # Replace with your OTLP endpoint URL
)

# Add the exporter to the TracerProvider
# tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))  # Add any span processors you need
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

# Register the TracerProvider
trace.set_tracer_provider(tracer_provider)

LangChainHandlerInstrumentor().instrument(tracer_provider=tracer_provider)

from dotenv import load_dotenv
import os
load_dotenv()

os.environ['OTEL_EXPORTER_OTLP_INSECURE'] = 'True'
os.environ["WATSONX_APIKEY"] = os.getenv("IAM_API_KEY")

# from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# parameters = {
#     GenParams.DECODING_METHOD: "sample",
#     GenParams.MAX_NEW_TOKENS: 30,
#     GenParams.MIN_NEW_TOKENS: 1,
#     GenParams.TEMPERATURE: 0.5,
#     GenParams.TOP_K: 50,
#     GenParams.TOP_P: 1,
# }

# from langchain.llms import WatsonxLLM

# watsonx_llm = WatsonxLLM(
#     model_id="google/flan-ul2",
#     url="https://us-south.ml.cloud.ibm.com",
#     project_id=os.getenv("PROJECT_ID"),
#     params=parameters,
# )

from genai.extensions.langchain import LangChainInterface
from genai.schemas import GenerateParams
from genai.credentials import Credentials

load_dotenv()
api_key = os.getenv("IBM_GENAI_KEY", None) 
api_url = os.getenv("IBM_GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url)

params = GenerateParams(
    decoding_method="sample",  # "greedy"
    max_new_tokens=20,
    min_new_tokens=10,
    temperature=0.7,
)

watson_langchain_model = LangChainInterface(model="google/flan-t5-xxl", params=params, credentials=creds)

from langchain.prompts import PromptTemplate
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI


# template = "Generate a random question about {topic}: Question: "
# prompt = PromptTemplate.from_template(template)

# from langchain.chains import LLMChain

# llm_chain = LLMChain(prompt=prompt, llm=watsonx_llm)
# llm_chain.run("dog")

llm = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], temperature=0.6)

tools = load_tools(["serpapi", "llm-math"], llm=watson_langchain_model)

agent = initialize_agent(
    tools, watson_langchain_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.agent.llm_chain.prompt.template)

agent.run("My monthly salary is 10000 KES, if i work for 10 months. How much is my total salary in USD in those 10 months.")
