from __future__ import annotations

from typing import Dict, Type

from agents.base import BaseAgent

# Pipeline agents
from agents.intake import IntakeAgent
from agents.parser import RequirementParserAgent
from agents.embedding import EmbeddingAgent
from agents.search import SemanticSearchAgent
from agents.compression import ContextCompressionAgent
from agents.ranking import RankingAgent

# Executive layer
from agents.executive_agents import (
    SupervisorAgent,
    PlannerAgent,
    ExecutionOptimizerAgent,
)

# Discovery layer
from agents.discovery.reflection import ReflectionAgent
from agents.discovery.match_intelligence import MatchIntelligenceAgent
from agents.discovery.market_intelligence import MarketIntelligenceAgent

# Trust layer
from agents.trust.trust_auditor import TrustAuditorAgent
from agents.trust.fraud import FraudAgent
from agents.trust.compliance import ComplianceAgent
from agents.trust.reputation import ReputationAgent

# Commercial layer
from agents.commercial.commercialization import CommercializationAgent
from agents.commercial.roi import ROIAgent
from agents.commercial.pricing import PricingAgent
from agents.commercial.acquisition_advisor import AcquisitionAdvisorAgent

# Vision layer
from agents.vision.vision_agents import (
    UIAuditAgent,
    UXAuditAgent,
    ArchitectureExplanationAgent,
    SecurityAuditAgent,
)

# Forking layer
from agents.forking.forking_agents import (
    ForkingAgent,
    SimilarityAgent,
    CloneIntelligenceAgent,
    ReusabilityAgent,
)

# Deployment layer
from agents.deployment.deployment_agents import (
    DeploymentSupervisorAgent,
    HealthMonitorAgent,
    IncidentAgent,
)

# Support layer
from agents.support.support_agents import (
    TicketTriageAgent,
    EscalationAgent,
    CustomerSuccessAgent,
)

AGENT_REGISTRY: Dict[str, Type[BaseAgent]] = {
    # Pipeline (6)
    "IntakeAgent": IntakeAgent,
    "RequirementParserAgent": RequirementParserAgent,
    "EmbeddingAgent": EmbeddingAgent,
    "SemanticSearchAgent": SemanticSearchAgent,
    "ContextCompressionAgent": ContextCompressionAgent,
    "RankingAgent": RankingAgent,
    
    # Executive (3)
    "SupervisorAgent": SupervisorAgent,
    "PlannerAgent": PlannerAgent,
    "ExecutionOptimizerAgent": ExecutionOptimizerAgent,

    # Discovery (3)
    "ReflectionAgent": ReflectionAgent,
    "MatchIntelligenceAgent": MatchIntelligenceAgent,
    "MarketIntelligenceAgent": MarketIntelligenceAgent,

    # Trust (4)
    "TrustAuditorAgent": TrustAuditorAgent,
    "FraudAgent": FraudAgent,
    "ComplianceAgent": ComplianceAgent,
    "ReputationAgent": ReputationAgent,

    # Commercial (4)
    "CommercializationAgent": CommercializationAgent,
    "ROIAgent": ROIAgent,
    "PricingAgent": PricingAgent,
    "AcquisitionAdvisorAgent": AcquisitionAdvisorAgent,

    # Vision (4)
    "UIAuditAgent": UIAuditAgent,
    "UXAuditAgent": UXAuditAgent,
    "ArchitectureExplanationAgent": ArchitectureExplanationAgent,
    "SecurityAuditAgent": SecurityAuditAgent,

    # Forking (4)
    "ForkingAgent": ForkingAgent,
    "SimilarityAgent": SimilarityAgent,
    "CloneIntelligenceAgent": CloneIntelligenceAgent,
    "ReusabilityAgent": ReusabilityAgent,

    # Deployment (3)
    "DeploymentSupervisorAgent": DeploymentSupervisorAgent,
    "HealthMonitorAgent": HealthMonitorAgent,
    "IncidentAgent": IncidentAgent,

    # Support (3)
    "TicketTriageAgent": TicketTriageAgent,
    "EscalationAgent": EscalationAgent,
    "CustomerSuccessAgent": CustomerSuccessAgent,
}

def get_agent(name: str) -> BaseAgent:
    cls = AGENT_REGISTRY.get(name)
    if not cls:
        raise ValueError(f"Unknown agent: {name}. Available: {list(AGENT_REGISTRY.keys())}")
    return cls()

AGENT_NAMES = list(AGENT_REGISTRY.keys())
TOTAL_AGENTS = len(AGENT_REGISTRY)
