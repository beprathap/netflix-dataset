{% macro generate_schema_name(custom_schema_name, node) -%}
    {# Respect schema overrides so curated layers land in PROD.DBT_TRANSFORM #}
    {%- if custom_schema_name is not none and (custom_schema_name | trim) != '' -%}
        {{ custom_schema_name }}
    {%- else -%}
        {{ target.schema }}
    {%- endif -%}
{%- endmacro %}
