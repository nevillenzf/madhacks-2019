import React from 'react';
import './App.css';
import SearchBar from './SearchBar';
import CompanyArea from './CompanyArea';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      companiesList: {}
    };
  }

  setCompanies(companies) {
    this.setState({companiesList: companies})
  }

  componentDidMount() {
    var url = "http://localhost:5000";
    axios.get("{url}/{path}")
      .then(res => {
        console.log(res.data);
      } )
  }

  render() {
    return (
      <>
        <SearchBar />
        <div style={{marginLeft: '20vw'}}>
          <CompanyArea data={this.state.companiesList} />
        </div>

      </>
    );
  }
}

export default App;
