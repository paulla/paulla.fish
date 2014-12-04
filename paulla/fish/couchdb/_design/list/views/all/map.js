function(doc) {
    if (doc.doc_type == "ToStore")
    {
	emit(doc.dtInserted, doc);
    }
}
