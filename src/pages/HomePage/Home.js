import React from 'react';
import { Element } from 'react-scroll';
import { InfoSection, Pricing } from '../../components';
import { homeObjTwo, homeObjFour } from './Data';

const Home = () => {
    return (
        <>
            <Element name="home">
                <InfoSection {...homeObjTwo} />
            </Element>
            <Element name="products">
                <Pricing />
            </Element>
            <InfoSection {...homeObjFour} />
        </>
    );
}

export default Home;
