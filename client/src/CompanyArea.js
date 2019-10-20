import React from 'react';
import './App.css';
import Company from './Company';

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
    var count = 1;
    for(const company of Object.entries(this.props.data)) {
      var temp = parseInt(company[0]) + 1;
      companyList.push (
        <Company key={company[0]} id={temp} data={company[1]} />
      )
    }

    return companyList;
  }

}

export default CompanyArea;
