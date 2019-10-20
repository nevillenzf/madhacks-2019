import React from 'react';
import './App.css';
import SearchBar from './SearchBar';
import CompanyArea from './CompanyArea';
import axios from 'axios';
import Navbar from 'react-bootstrap/Navbar';
import Logo from "./Footprintr_Logo_2.png";
//import Image from 'react-bootstrap/Image';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      companiesList: {}
    };
  }

  setCompanies(companies) {
    this.setState({companiesList: companies.data})
  }

  componentDidMount() {
    var url = "https://footprintr-backend.appspot.com/companies";
    axios.get(url)
      .then(res => {
        this.setCompanies(res);
      } )
  }

  render() {
    return (
      <>
        <div>
          <Navbar>
            <img src={Logo} alt="Footprint Logo" style={{height: "100px", width: "100px"}}/>
          </Navbar>
          <SearchBar setCompanies={(companies) => this.setCompanies(companies)} company={this.state.companiesList} data={this.state.companiesList}/>
        </div>

        <div style={{marginLeft: '20vw'}}>
          <CompanyArea data={this.state.companiesList} />
        </div>

      </>
    );
  }
}

export default App;
