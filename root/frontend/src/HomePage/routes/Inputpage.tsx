import Navbar from '../components/Navbar'
import React  from 'react';

import Footer from '../components/footer';
import { Form } from '../../Form/Form';
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