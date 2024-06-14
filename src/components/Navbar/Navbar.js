import React, { useState, useEffect } from 'react';
import { Link as ScrollLink } from 'react-scroll';
import { Nav, 
    NavbarContainer, 
    NavLogo, 
    NavIcon, 
    HamburgerIcon,
    NavMenu,
    NavItem,
    NavLinks
 } from './Navbar.elements';
import { FaTimes, FaBars } from 'react-icons/fa';
import { IconContext } from 'react-icons/lib';

function Navbar() {
    const [click, setClick] = useState(false);
    const [button, setButton] = useState(true);

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    const showButton = () => {
        if (window.innerWidth <= 960) {
            setButton(false);
        } else {
            setButton(true);
        }
    };

    useEffect(() => {
        showButton();
    }, []);

    window.addEventListener('resize', showButton);

    return (
        <>
            <IconContext.Provider value={{ color: '#fff' }}>
                <Nav>
                    <NavbarContainer>
                        <NavLogo to='/'>
                            <NavIcon />
                            One Click AI
                        </NavLogo>
                        <HamburgerIcon onClick={handleClick}>
                            {click ? <FaTimes /> : <FaBars />}
                        </HamburgerIcon>
                        <NavMenu onClick={handleClick} click={click}>
                            <NavItem>
                                <NavLinks as={ScrollLink} to='home' smooth={true} duration={500} onClick={closeMobileMenu}>
                                    Home
                                </NavLinks>
                            </NavItem>
                            <NavItem>
                                <NavLinks as={ScrollLink} to='products' smooth={true} duration={500} onClick={closeMobileMenu}>
                                    Products
                                </NavLinks>
                            </NavItem>
                            <NavItem>
                                <NavLinks as={ScrollLink} to='contact' smooth={true} duration={500} onClick={closeMobileMenu}>
                                    Contact
                                </NavLinks>
                            </NavItem>
                        </NavMenu>
                    </NavbarContainer>
                </Nav>
            </IconContext.Provider>
        </>
    );
}

export default Navbar;
