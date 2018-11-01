Install Solr 7.5.0

Start solr in schemaless mode

`./bin/solr start -e schemaless`

Create a new core

`./bin/solr create -c zooma_rules`

Load the rules

`./bin/post -p 8983 -c zooma_rules ../rules.json`

Run a query

```
(_childDocuments_.propertyType:(tumortype AND origintissue AND samplediagnosis)) AND
(_childDocuments_.propertyValue: Blood AND_childDocuments_.propertyValue: "acute myeloid leukemia" AND
_childDocuments_.propertyValue: "Primary"
) AND
tag.propertyType : samplediagnosis
```