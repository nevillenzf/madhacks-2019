import React from 'react';
import './App.css';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';

class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.search = React.createRef();
  }

  render() {
    return (
      <>
        <Card style={{height: 'calc(100vh - 10px)', width: 'calc(20vw - 5px)', marginLeft: '5px',  position: 'fixed', backgroundColor: '#98ad97', color: '#ffffff'}}>
          <Card.Body style={{padding: '10px'}}>
            <Card.Title>Filter Companies</Card.Title>
            <Form>
              <div className="form-group">
                <label>Search for Company</label>
                <input className="form-control" id="searchCompany" autoComplete="off" placeholder="Company Name" ref={this.search}/>
              </div>
            </Form>

          </Card.Body>
        </Card>
      </>
    )
  }

  setCompanies(){
    this.props.setCourses(this.searchCompanies);
  }

  searchCompanies(){
    var filteredCompanies = [];

    for(const company of Object.values(this.props.data)) {
        if (company.toLowerCase() == this.search.toLowerCase()){
            filteredCompanies.push(company);
        }
    }
    return filteredCompanies;

  }

}

export default SearchBar;
