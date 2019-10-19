import React from 'react';
import './App.css';
import Company from './Company';
import CardColumns from 'react-bootstrap/CardColumns';

class CompanyArea extends React.Component {
  render() {
    return (
      <div style={{margin: '5px'}}>

        {this.getCompanies()}
    
      </div>
    )
  }

  getCompanies() {
    let companyList = [];
    for(var i = 0; i < 25; i++) {
      companyList.push (
        <Company />
      )
    }

    /*
    for(const company of Object.entries(this.props.data)) {
      companyList.push (
        <Company key={companyList[0]} data={companyList[1]}/>
      )
    }
    */

    return companyList;
  }

}

export default CompanyArea;
