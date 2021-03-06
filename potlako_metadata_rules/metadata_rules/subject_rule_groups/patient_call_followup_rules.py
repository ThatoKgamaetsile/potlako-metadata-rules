from edc_constants.constants import YES
from edc_metadata import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, P, register

app_label = 'potlako_subject'


@register()
class PatientCallFollowUpRuleGroup(CrfRuleGroup):

    transport = CrfRule(
        predicate=P('transport_support', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.transport'])

    investigations_ordered = CrfRule(
        predicate=P('investigations_ordered', 'eq', 'ordered'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.investigationsordered'])

    investigations_resulted = CrfRule(
        predicate=P('investigations_ordered', 'eq', 'resulted'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.investigationsresulted'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.patientcallfollowup'
