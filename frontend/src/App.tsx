import './App.css';
import { Button } from '@ui/button';
import { Checkbox } from '@ui/checkbox';
import { Input } from '@ui/input';
import { RadioGroup, RadioGroupItem } from '@ui/radio-group';

function App() {

  return (
    <div className='mx-auto max-w-2xl p-4'>
      <div>
        <Button variant="primary">Primary Button</Button>
      </div>
      <div className='mt-4'>
        <label className="flex items-center gap-2">
          <Checkbox />
          <span>
            Accept terms and conditions.
          </span>
        </label>
      </div>
      <div className='mt-4'>
        <Input
          type="text"
          placeholder="Enter your name"
          className="mt-4"
        />
      </div>
      <div className='mt-4'>
        <RadioGroup
          className="RadioGroupRoot"
          defaultValue="default"
          aria-label="View density"
        >
          <div className='flex items-center gap-1'>
            <RadioGroupItem className="RadioGroupItem" value="default" id="r1" />
            <label className="Label" htmlFor="r1">
              Default
            </label>
          </div>
          <div className='flex items-center gap-1'>
            <RadioGroupItem className="RadioGroupItem" value="comfortable" id="r2" />
            <label className="Label" htmlFor="r2">
              Comfortable
            </label>
          </div>
          <div className='flex items-center gap-1'>
            <RadioGroupItem className="RadioGroupItem" value="compact" id="r3" />
            <label className="Label" htmlFor="r3">
              Compact
            </label>
          </div>
        </RadioGroup>
      </div>
    </div>
  )
}

export default App
