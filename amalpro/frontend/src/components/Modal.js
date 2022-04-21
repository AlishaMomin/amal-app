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
                defaultvalue={this.state.activeItem.fullNameCustomer}
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
                defaultvalue={this.state.activeItem.cnicCustomer}
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
                defaultvalue={this.state.activeItem.addressCustomer}
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
                defaultvalue={this.state.activeItem.cityCustomer}
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
                defaultvalue={this.state.activeItem.dobCustomer}
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
                defaultvalue={this.state.activeItem.ReviewCustomer}
                onChange={this.handleChange}
                placeholder="Say Something!"
              />
            </FormGroup>
          </Form>
        </ModalBody>

        <ModalHeader toggle={toggle}>ServiceProviders Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="ServiceProviders-name">Full Name</Label>
              <Input
                type="text"
                id="ServiceProviders-name"
                name="name"
                defaultvalue={this.state.activeItem.fullNameSP}
                onChange={this.handleChange}
                placeholder="Enter ServiceProviders Full Name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-cnic">CNIC Number</Label>
              <Input
                type="text"
                id="ServiceProviders-cnic"
                name="cnic"
                defaultvalue={this.state.activeItem.cnicSP}
                onChange={this.handleChange}
                placeholder="42201-3748392-7"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-address">Address</Label>
              <Input
                type="text"
                id="ServiceProviders-address"
                name="address"
                defaultvalue={this.state.activeItem.addressSP}
                onChange={this.handleChange}
                placeholder="A-245, Block-5, Gulshan-e-Iqbal"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-city">City</Label>
              <Input
                type="text"
                id="ServiceProviders-city"
                name="city"
                defaultvalue={this.state.activeItem.citySP}
                onChange={this.handleChange}
                placeholder="Karachi"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-date">Date of Birth</Label>
              <Input
                type="date"
                id="ServiceProviders-dob"
                name="dob"
                defaultvalue={this.state.activeItem.dobSP}
                onChange={this.handleChange}
                placeholder="07/12/1999"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-Language">Language</Label>
              <Input
                type="text"
                id="ServiceProviders-Language"
                name="Language"
                defaultvalue={this.state.activeItem.languageSP}
                onChange={this.handleChange}
                placeholder="Urdu or English"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        
        <ModalHeader toggle={toggle}>Booking Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="Booking-date">date</Label>
              <Input
                type="date"
                id="Booking-date"
                name="date"
                defaultvalue={this.state.activeItem.bookingDate}
                onChange={this.handleChange}
                placeholder="Enter Booking date"
              />
            </FormGroup>
            <FormGroup>
              <Label for="Booking-slot">CNIC Number</Label>
              <Input
                type="text"
                id="Booking-slot"
                name="slot"
                defaultvalue={this.state.activeItem.bookingSlot}
                onChange={this.handleChange}
                placeholder="12:30"
              />
            </FormGroup>
            <FormGroup>
              <Label for="Booking-Service type">service type</Label>
              <Input
                type="text"
                id="Booking-Service type"
                name="Service type"
                defaultvalue={this.state.activeItem.serviceType}
                onChange={this.handleChange}
                placeholder="cleaning"
              />
            </FormGroup>
            <FormGroup>
              <Label for="ServiceProviders-ID">Service Provider ID</Label>
              <Input
                type="text"
                id="ServiceProviders-ID"
                name="ID"
                defaultvalue={this.state.activeItem.ServiceProviderID}
                onChange={this.handleChange}
                placeholder="11111"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        

        <ModalHeader toggle={toggle}>Listing Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="Charges">Charges</Label>
              <Input
                type="text"
                id="Charges"
                name="Charges"
                defaultvalue={this.state.activeItem.Charges}
                onChange={this.handleChange}
                placeholder="Enter Charges"
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