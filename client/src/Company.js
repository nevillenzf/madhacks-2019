import React from 'react';
import './App.css';
import Card from 'react-bootstrap/Card';

class Company extends React.Component {
  render() {
    return (
      <div>
        <Card class="companyCard" style={{backgroundColor: '#66be41', marginTop: '5px', marginBottom: '5px', padding: '10px', paddingTop: '2%'}}>
          <Card.Body>
            <Card.Subtitle style={{color: '#416732', backgroundColor: '#a0da5b', padding: '1%'}}>[Company Name]</Card.Subtitle>
            <Card.Title style={{color:"#ffffff", padding: '1%'}}>[Company Score]</Card.Title>
            <Card.Text id="expandInformation" style={{paddingTop: '5px'}}>
            </Card.Text>
          </Card.Body>
        </Card>
      </div>
    )
  }
}

export default Company;
