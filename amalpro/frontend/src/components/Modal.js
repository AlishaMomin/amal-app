import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Customer Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="customer-name">Full Name</Label>
              <Input
                type="text"
                id="customer-name"
                name="name"
                value={this.state.activeItem.fullNameCustomer}
                onChange={this.handleChange}
                placeholder="Enter Customers Full Name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-cnic">CNIC Number</Label>
              <Input
                type="text"
                id="customer-cnic"
                name="cnic"
                value={this.state.activeItem.cnicCustomer}
                onChange={this.handleChange}
                placeholder="42201-3748392-7"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-address">Address</Label>
              <Input
                type="text"
                id="customer-address"
                name="address"
                value={this.state.activeItem.addressCustomer}
                onChange={this.handleChange}
                placeholder="A-245, Block-5, Gulshan-e-Iqbal"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-city">City</Label>
              <Input
                type="text"
                id="customer-city"
                name="city"
                value={this.state.activeItem.cityCustomer}
                onChange={this.handleChange}
                placeholder="Karachi"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-date">Date of Birth</Label>
              <Input
                type="date"
                id="customer-dob"
                name="dob"
                value={this.state.activeItem.dobCustomer}
                onChange={this.handleChange}
                placeholder="07/12/1999"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-review">Reviews</Label>
              <Input
                type="text"
                id="customer-review"
                name="review"
                value={this.state.activeItem.ReviewCustomer}
                onChange={this.handleChange}
                placeholder="Say Something!"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}