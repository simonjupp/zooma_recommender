Install Solr 7.5.0

Start solr in schemaless mode

`./bin/solr start -e schemaless`

Create a new core

`./bin/solr create -c zooma_rules`

Load the rules

`./bin/post -p 8983 -c zooma_rules ../rules.json`

Run a query

```
(properties.propertyType:(tumortype AND origintissue AND samplediagnosis)) AND
(properties.propertyValue: Blood AND properties.propertyValue: "acute myeloid leukemia" AND
properties.propertyValue: "Primary"
) AND
tag.propertyType : samplediagnosis
```