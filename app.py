from flask import Flask, render_template, url_for, redirect
from rdflib import Graph

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template("index.html")

@app.route("/update/", methods=['POST'])
def update():
    g = Graph()
    g.parse("SAMPLEDATA.rdf")
    # g.update("""INSERT DATA { <z:> a <c:> }""")
    return render_template('update.html');

@app.route("/query/", methods=['POST', 'GET'])
def query():
    return render_template('query.html');
    
@app.route("/queryWork/", methods=['POST'])
def queryWork():
    g = Graph()
    g.parse("SAMPLEDATA.rdf")
    knows_query = """
    SELECT ?x ?y
    WHERE {
        ?x <http://www.semanticweb.org/win11/ontologies/2023/3/untitled-ontology-13#worksFor> ?y .
    }
    """
    qres = g.query(knows_query)
    Person = []
    Employer = []
    for row in qres:
        person = str(row.x)
        Person.append(person[72:])
        employer = str(row.y)
        Employer.append(employer[72:])
    Len = len(Person)
    return render_template('work.html', Person = Person, Employer = Employer, Len = Len);

@app.route("/queryName/", methods=['POST'])
def queryName():
    g = Graph()
    g.parse("SAMPLEDATA.rdf")
    knows_query = """
    SELECT ?x ?y
    WHERE {
        ?x <http://www.semanticweb.org/win11/ontologies/2023/3/untitled-ontology-13#hasName> ?y .
    }
    """
    qres = g.query(knows_query)
    Person = []
    Name = []
    for row in qres:
        person = str(row.x)
        Person.append(person[72:])
        name = str(row.y)
        Name.append(name[72:])
    Len = len(Name)
    return render_template('name.html', Person = Person, Name = Name, Len = Len);

@app.route("/queryEligible/", methods=['POST'])
def queryEligible():
    g = Graph()
    g.parse("SAMPLEDATA.rdf")
    knows_query = """
    SELECT ?x ?y
    WHERE {
        ?x <http://www.semanticweb.org/win11/ontologies/2023/3/untitled-ontology-13#eligibleFor> ?y .
    }
    """
    qres = g.query(knows_query)
    Person = []
    Name = []
    for row in qres:
        person = str(row.x)
        Person.append(person[72:])
        name = str(row.y)
        Name.append(name[72:])
    Len = len(Name)
    return render_template('eligible.html', Person = Person, Name = Name, Len = Len);

if __name__ == "__main__":
    app.run(debug = True)