import React from 'react';
import './App.css';
import Card from 'react-bootstrap/Card';

class Company extends React.Component {
  render() {
    return (
      <div>
        <Card className="companyCard" style={{backgroundColor: '#416732', marginTop: '5px', marginBottom: '5px', padding: '10px', paddingTop: '2%'}}>
          <Card.Body>
            <Card.Subtitle style={{color: '#416732', backgroundColor: '#a0da5b', padding: '1%'}}>{this.props.id}: {this.props.data.count} {this.props.data.company_name}</Card.Subtitle>
            <Card.Title style={{color:"#ffffff", paddingTop: '1%'}}>Score: {this.props.data.calc_score}</Card.Title>
            <Card.Text id="expandInformation" style={{paddingTop: '5px'}}>
            </Card.Text>
          </Card.Body>
        </Card>
      </div>
    )
  }
}

export default Company;
