import React from 'react';
import './App.css';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';

class SearchBar extends React.Component {
  render() {
    console.log("testing");
    return (
      <>
        <Card style={{height: 'calc(100vh - 10px)', width: 'calc(20vw - 5px)', marginLeft: '5px',  position: 'fixed', backgroundColor: '#a0da5b', color: '#416732'}}>
          <Card.Body style={{padding: '10px'}}>
            <Card.Title>Filter Companies</Card.Title>
            <Form>
              <div class="form-group">
                <label>Search for Company</label>
                <input class="form-control" id="searchCompany" placeholder="Company Name" />
              </div>
            </Form>

          </Card.Body>
        </Card>
      </>
    )
  }
}

export default SearchBar;
