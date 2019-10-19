import React from 'react';
import './App.css';
import Card from 'react-bootstrap/Card';

class Company extends React.Component {
  render() {
    return (
      <div>
        <Card style={{marginTop: '5px', marginBottom: '5px', padding: '10px'}}>
          <Card.Body>
            <Card.Title>Company Name</Card.Title>
            <Card.Subtitle style={{color:"#f54b42"}}>Company Score</Card.Subtitle>
            <Card.Text id="expandInformation" style={{paddingTop: '5px'}}>
            </Card.Text>
          </Card.Body>
        </Card>
      </div>
    )
  }
}

export default Company;
