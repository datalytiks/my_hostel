import {Component, useState} from '@odoo/owl';

export class Counter extends Component{
    static template = "my_hostel.Counter_Template";

    setup(){
        this.state = useState({count: 0});
    }

    increment(){
        this.state.count++;
    }

}