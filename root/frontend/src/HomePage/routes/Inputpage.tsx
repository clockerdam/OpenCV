import Navbar from '../components/Navbar'
import React  from 'react';

import Footer from '../components/Footer';
import { Form } from '../../InputView/Form/Form';
function Home(){
    return (
        <>
        <Navbar />
        <Form />
        <Footer/>
        </>
    );
}
export default Home;